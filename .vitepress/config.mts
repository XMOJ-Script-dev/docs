import { defineConfig } from 'vitepress'
import mathjax3 from 'markdown-it-mathjax3'

const customElements = [
  'mjx-container', 'mjx-assistive-mml', 'math', 'maction', 'maligngroup',
  'malignmark', 'menclose', 'merror', 'mfenced', 'mfrac', 'mi', 'mlabeledtr',
  'mlongdiv', 'mmultiscripts', 'mn', 'mo', 'mover', 'mpadded', 'mphantom',
  'mprescripts', 'mroot', 'mrow', 'ms', 'mscarries', 'mscarry', 'msgroup',
  'mstack', 'msup', 'msub', 'msubsup', 'mtable', 'mtd', 'mtext', 'mtr',
  'munder', 'munderover', 'semantics', 'annotation', 'annotation-xml'
]

export default defineConfig({
  title: 'XMOJ-Script 文档',
  description: 'XMOJ-Script（小明的OJ增强脚本）的安装和使用说明',
  lang: 'zh-CN',

  head: [
    ['link', { rel: 'icon', href: '/logo.png' }],
    ['link', { rel: 'preconnect', href: 'https://fonts.loli.net' }],
    ['link', { rel: 'stylesheet', href: 'https://fonts.loli.net/css2?family=Playfair+Display:wght@400;700&family=Source+Serif+4:wght@400;600;700&family=JetBrains+Mono:wght@400;500&display=swap' }],
  ],

  markdown: {
    config: (md) => {
      md.use(mathjax3)
    },
  },

  vue: {
    template: {
      compilerOptions: {
        isCustomElement: (tag) => customElements.includes(tag),
      },
    },
  },

  themeConfig: {
    logo: '/logo.png',

    nav: [
      { text: '安装', link: '/guide/installation' },
      {
        text: '功能介绍',
        items: [
          { text: '功能总览', link: '/features/' },
          { text: '用户评分', link: '/features/rating' },
          { text: '图床', link: '/features/image-hosting' },
          { text: '获取测试点数据', link: '/features/get-data' },
          { text: '自动提交当年代码', link: '/features/auto-handin' },
        ],
      },
      {
        text: '社区',
        items: [
          { text: '徽章/Tag', link: '/community/badges' },
          { text: '贡献指南', link: '/community/contributing' },
        ],
      },
      {
        text: '配套应用',
        items: [
          { text: '短消息在线看', link: '/apps/messages' },
        ],
      },
      { text: '常见问题', link: '/qa/discussion' },
      { text: '官网', link: 'https://www.xmoj-script.uk' },
    ],

    sidebar: [
      {
        text: '快速开始',
        items: [
          { text: '安装指南', link: '/guide/installation' },
        ],
      },
      {
        text: '功能介绍',
        items: [
          { text: '功能总览', link: '/features/' },
          { text: '用户评分', link: '/features/rating' },
          { text: '图床', link: '/features/image-hosting' },
          { text: '获取测试点数据', link: '/features/get-data' },
          { text: '自动提交当年代码', link: '/features/auto-handin' },
        ],
      },
      {
        text: '配套应用',
        items: [
          { text: '短消息在线看', link: '/apps/messages' },
        ],
      },
      {
        text: '社区',
        items: [
          { text: '徽章/Tag', link: '/community/badges' },
          { text: '贡献指南', link: '/community/contributing' },
        ],
      },
      {
        text: '更多',
        items: [
          { text: '常见问题', link: '/qa/discussion' },
          { text: '使用条款', link: 'https://www.xmoj-script.uk/terms.html' },
          { text: '隐私说明', link: 'https://www.xmoj-script.uk/privacy.html' },
          { text: '未成年人保护', link: 'https://www.xmoj-script.uk/child-protection.html' },
        ],
      },
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/XMOJ-Script-dev/XMOJ-Script' },
    ],

    footer: {
      message: '以 GPL-3.0 开源 · <a href="https://www.xmoj-script.uk/terms.html">使用条款</a> · <a href="https://www.xmoj-script.uk/privacy.html">隐私说明</a>',
      copyright: '原项目作者 langningchen · 由 XMOJ-Script-dev 维护',
    },

    editLink: {
      pattern: 'https://github.com/XMOJ-Script-dev/docs/edit/master/:path',
      text: '在 GitHub 上改这一页',
    },

    lastUpdated: {
      text: '最后更新于',
    },

    docFooter: {
      prev: '上一页',
      next: '下一页',
    },

    outline: {
      level: [2, 3],
      label: '本页目录',
    },

    returnToTopLabel: '回到顶部',
    sidebarMenuLabel: '菜单',
    darkModeSwitchLabel: '主题',
    lightModeSwitchTitle: '切换到浅色模式',
    darkModeSwitchTitle: '切换到深色模式',

    search: {
      provider: 'local',
      options: {
        locales: {
          root: {
            translations: {
              button: {
                buttonText: '搜索文档',
                buttonAriaLabel: '搜索文档',
              },
              modal: {
                noResultsText: '无法找到相关结果',
                resetButtonTitle: '清除查询条件',
                footer: {
                  selectText: '选择',
                  navigateText: '切换',
                  closeText: '关闭',
                },
              },
            },
          },
        },
      },
    },
  },
})
