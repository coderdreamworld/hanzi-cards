const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');

const source = fs.readFileSync(path.join(__dirname, '..', 'analytics.js'), 'utf8');

function run(hostname = 'coderdreamworld.github.io') {
  const pageEvents = {};
  const head = [];
  const document = {
    referrer: 'https://coderdreamworld.github.io/hanzi-cards/index.html?from=hub',
    head: {appendChild(item) {head.push(item);}},
    createElement(tag) {return {tag};}
  };
  const location = {
    hostname, origin: 'https://coderdreamworld.github.io',
    pathname: '/hanzi-cards/shizi-422.html', search: '?n=17'
  };
  const window = {addEventListener(name, fn) {pageEvents[name] = fn;}};
  vm.runInNewContext(source, {window, document, location, URL, Date, Object});
  return {head, window, pageEvents};
}

const production = run();
const scripts = production.head.filter(item => item.tag === 'script');
assert.equal(scripts.length, 1, 'load one Google tag without a consent click');
assert.equal(scripts[0].async, true, 'do not block page rendering');
assert.equal(scripts[0].src, 'https://www.googletagmanager.com/gtag/js?id=G-V23C1X2DQX');
const config = production.window.dataLayer.find(args => args[0] === 'config');
assert.equal(config[2].page_location, 'https://coderdreamworld.github.io/hanzi-cards/shizi-422.html');
assert.equal(config[2].page_referrer, 'https://coderdreamworld.github.io/hanzi-cards/index.html');
assert.equal(config[2].allow_google_signals, false);
const count = production.window.dataLayer.length;
production.pageEvents.pageshow({persisted: false});
assert.equal(production.window.dataLayer.length, count, 'avoid duplicate first pageview');
production.pageEvents.pageshow({persisted: true});
assert.equal(production.window.dataLayer.at(-1)[1], 'page_view', 'count back-forward cache visit');

assert.equal(run('localhost').head.length, 0, 'ignore local previews');
console.log('自动接入、异步加载、URL 隐私处理与返回页面计数均通过');
