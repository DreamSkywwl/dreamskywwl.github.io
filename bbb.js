// {id: 1, name: "Google", url: "https://www.google.com", category: "dev"},

let arr = [
  { name: '公司官网', url: 'https://office.inspur.com/', category: 'work' },
  { name: '工时登记', url: 'https://devops.inspur.com/', category: 'work' },
  { name: '百度搜索', url: 'https://www.baidu.com/', category: 'dev' },
  { name: '百度翻译', url: 'https://fanyi.baidu.com/mtpe-individual/transText#/', category: 'dev' },
  { name: '百度文心助手', url: 'https://chat.baidu.com/search?isShowHello=1&extParams=%7B%22out_enter_type%22%3A%22home_aiinput_askai%22%2C%22enter_type%22%3A%22sidebar_dialog%22%7D', category: 'dev' },

  { name: '必应搜索', url: 'https://cn.bing.com/', category: 'dev' },
  { name: '百度地图', url: 'https://map.baidu.com/', category: 'dev' },
  { name: '豆包AI', url: 'https://www.doubao.com/chat/', category: 'dev' },
  { name: 'JSON在线', url: 'https://www.bejson.com/jsoneditoronline/', category: 'dev' },
  { name: '随机密码', url: 'https://suijimimashengcheng.bmcx.com/', category: 'dev' },
  { name: '调色板', url: 'https://www.bejson.com/ui/getcolor/', category: 'dev' },
  { name: '草料二维码', url: 'https://cli.im/', category: 'dev' },
  { name: '阿里life', url: 'https://www.aliyundrive.com/drive/home', category: 'life' },
  { name: '百度life', url: 'https://pan.baidu.com/disk/main#/index?category=all', category: 'life' },
  { name: '夸克life', url: 'https://pan.quark.cn/list#/list/all', category: 'life' },



  { name: '知乎', url: 'https://www.zhihu.com/', category: 'study' },
  { name: '掘金', url: 'https://juejin.cn/', category: 'study' },
  { name: 'HelloGithub', url: 'https://hellogithub.com/', category: 'study' },
  { name: '山东联通', url: 'https://www.10010.com/wt_service_web/index.html#/', category: 'study' },
  { name: 'uniapp', url: 'https://uniapp.dcloud.net.cn/', category: 'study' },



  { name: '解析图片', url: 'https://dreamskywwl.github.io/downloadPic.html', category: 'other' },
  { name: 'Github', url: 'https://github.com/DreamSkywwl', category: 'other' },

]

let arrOptions = []
for (let index = 0; index < arr.length; index++) {
  const element = arr[index];
  element.id = index + 1
  arrOptions.push(element)
}
// console.log('arr>-->:', JSON.stringify(arrOptions));

const fs = require('fs');
let fileName = 'htmlTag2.json'
// 将数据写入aaa.json文件
fs.writeFile(fileName, JSON.stringify(arrOptions, null, 2), (err) => {
  if (err) {
    console.error('写入文件时出错:', err);
    return;
  }
  console.log(`成功创建${fileName}文件并写入数据`);
});

/* 
{ name: '', url: '', category: 'dev' },
  { name: '', url: '', category: '' },
  { name: '', url: '', category: '' },
  { name: '', url: '', category: '' },
  { name: '', url: '', category: '' },
*/