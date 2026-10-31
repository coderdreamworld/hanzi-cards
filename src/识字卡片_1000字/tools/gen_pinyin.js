const fs = require('fs');
const { pinyin } = require('pinyin-pro');
const zikuSrc = fs.readFileSync('../字库1000.py', 'utf8');
const chars = [...new Set(zikuSrc.match(/[\u4e00-\u9fff]/g).filter(c => !'一二三四五六七八九十幼儿识字卡片字库与分组版组完全致顺备注变主题并或新构运自检总数重复包含运行'.includes(c)))];
// 更稳妥：直接从 python 导出的清单拿
