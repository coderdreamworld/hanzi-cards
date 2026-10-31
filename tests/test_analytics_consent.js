const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');

const source = fs.readFileSync(path.join(__dirname, '..', 'analytics.js'), 'utf8');

function run(initialChoice, hostname = 'coderdreamworld.github.io') {
  const stored = initialChoice ? {'hz.analytics.consent.v1': initialChoice} : {};
  const pageEvents = {};
  const head = [];
  const body = [];
  let reloads = 0;
  function element(tag) {
    const buttons = {};
    return {
      tag, id: '', children: [], listeners: {},
      setAttribute() {},
      appendChild(child) { this.children.push(child); },
      addEventListener(name, fn) { this.listeners[name] = fn; },
      querySelector(selector) {
        if (!buttons[selector]) buttons[selector] = element('button');
        return buttons[selector];
      },
      remove() {
        const list = body.includes(this) ? body : head;
        list.splice(list.indexOf(this), 1);
      }
    };
  }
  const document = {
    readyState: 'complete',
    referrer: 'https://coderdreamworld.github.io/hanzi-cards/index.html?from=hub',
    head: {appendChild(item) {head.push(item);}},
    body: {appendChild(item) {body.push(item);}},
    createElement: element,
    getElementById(id) {return [...head, ...body].find(item => item.id === id);}
  };
  const location = {
    hostname, origin: 'https://coderdreamworld.github.io',
    pathname: '/hanzi-cards/shizi-422.html',
    reload() {reloads++;}
  };
  const window = {addEventListener(name, fn) {pageEvents[name] = fn;}};
  const localStorage = {
    getItem(key) {return stored[key] || null;},
    setItem(key, value) {stored[key] = value;}
  };
  vm.runInNewContext(source, {window, document, location, localStorage, URL, Date, Object});
  return {head, body, stored, window, pageEvents, get reloads() {return reloads;}};
}

function googleScripts(env) {
  return env.head.filter(item => item.tag === 'script' && item.src?.includes('googletagmanager.com'));
}

const first = run();
assert.equal(googleScripts(first).length, 0, 'no Google request before consent');
const notice = first.body.find(item => item.id === 'hz-analytics-choice');
assert.ok(notice, 'show a non-blocking choice');
notice.querySelector('[data-choice="yes"]').listeners.click();
assert.equal(googleScripts(first).length, 1, 'load one Google tag after consent');
assert.equal(first.stored['hz.analytics.consent.v1'], 'yes');
const config = first.window.dataLayer.find(args => args[0] === 'config');
assert.equal(config[2].page_location, 'https://coderdreamworld.github.io/hanzi-cards/shizi-422.html');
assert.equal(config[2].page_referrer, 'https://coderdreamworld.github.io/hanzi-cards/index.html');
const count = first.window.dataLayer.length;
first.pageEvents.pageshow({persisted: false});
assert.equal(first.window.dataLayer.length, count, 'avoid duplicate first pageview');
first.pageEvents.pageshow({persisted: true});
assert.equal(first.window.dataLayer.at(-1)[1], 'page_view', 'count back-forward cache visit');

const denied = run();
denied.body.find(item => item.id === 'hz-analytics-choice')
  .querySelector('[data-choice="no"]').listeners.click();
assert.equal(googleScripts(denied).length, 0);
assert.equal(denied.stored['hz.analytics.consent.v1'], 'no');
assert.equal(googleScripts(run('no')).length, 0, 'keep declining on later pages');
assert.equal(googleScripts(run('yes')).length, 1, 'keep consent on later pages');
assert.equal(googleScripts(run(undefined, 'localhost')).length, 0, 'ignore local previews');
console.log('统计同意、拒绝、URL 隐私处理与返回页面计数均通过');
