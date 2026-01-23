// {id: 1, title: "Google", url: "https://www.google.com", category: "工具"},

let arr = [
  { title: '公司官网', url: 'https://office.inspur.com/', category: '工作' },
  { title: '工时登记', url: 'https://devops.inspur.com/', category: '工作' },
  { title: '百度搜索', url: 'https://www.baidu.com/', category: '工具' },
  { title: '百度翻译', url: 'https://fanyi.baidu.com/mtpe-individual/transText#/', category: '工具' },
  { title: '百度文心助手', url: 'https://chat.baidu.com/search?isShowHello=1&extParams=%7B%22out_enter_type%22%3A%22home_aiinput_askai%22%2C%22enter_type%22%3A%22sidebar_dialog%22%7D', category: '工具' },

  { title: '必应搜索', url: 'https://cn.bing.com/', category: '工具' },
  { title: '百度地图', url: 'https://map.baidu.com/', category: '工具' },
  { title: '豆包AI', url: 'https://www.doubao.com/chat/', category: '工具' },
  { title: 'JSON在线', url: 'https://www.bejson.com/jsoneditoronline/', category: '工具' },
  { title: '随机密码', url: 'https://suijimimashengcheng.bmcx.com/', category: '工具' },
  { title: '调色板', url: 'https://www.bejson.com/ui/getcolor/', category: '工具' },
  { title: '草料二维码', url: 'https://cli.im/', category: '工具' },
  { title: '阿里网盘', url: 'https://www.aliyundrive.com/drive/home', category: '网盘' },
  { title: '百度网盘', url: 'https://pan.baidu.com/disk/main#/index?category=all', category: '网盘' },
  { title: '夸克网盘', url: 'https://pan.quark.cn/list#/list/all', category: '网盘' },



  { title: '知乎', url: 'https://www.zhihu.com/', category: '学习' },
  { title: '掘金', url: 'https://juejin.cn/', category: '学习' },
  { title: 'HelloGithub', url: 'https://hellogithub.com/', category: '学习' },
  { title: '山东联通', url: 'https://www.10010.com/wt_service_web/index.html#/', category: '学习' },
  { title: 'uniapp', url: 'https://uniapp.dcloud.net.cn/', category: '学习' },



  { title: '解析图片', url: 'https://dreamskywwl.github.io/downloadPic.html', category: '其他' },

]

let arrOptions = []
for (let index = 0; index < arr.length; index++) {
  const element = arr[index];
  element.id = index + 1
  arrOptions.push(element)
}
console.log('arr>-->:', JSON.stringify(arrOptions));
/* 
{ title: '', url: '', category: '工具' },
  { title: '', url: '', category: '' },
  { title: '', url: '', category: '' },
  { title: '', url: '', category: '' },
  { title: '', url: '', category: '' },
*/