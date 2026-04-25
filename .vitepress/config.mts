import { defineConfig } from 'vitepress'

export default defineConfig({
  title: '小明的OJ增强脚本',
  description: '小明的OJ增强脚本用户帮助文档',
  lang: 'zh-CN',

  head: [
    ['link', { rel: 'icon', href: '/logo.png' }],
  ],

  themeConfig: {
    logo: '/logo.png',

    nav: [
      { text: '首页', link: '/' },
      { text: '安装指南', link: '/guide/installation' },
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
          { text: 'ELXMOJ 桌面客户端', link: '/apps/elxmoj' },
        ],
      },
      {
        text: '更多',
        items: [
          { text: '常见问题', link: '/qa/discussion' },
          { text: '用户协议', link: '/legal/eula' },
        ],
      },
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
          { text: 'ELXMOJ 桌面客户端', link: '/apps/elxmoj' },
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
          { text: '用户协议', link: '/legal/eula' },
        ],
      },
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/XMOJ-Script-dev/XMOJ-Script' },
    ],

    footer: {
      message: '基于 GPLv3 许可证发布',
      copyright: 'Copyright © XMOJ-Script-dev',
    },

    editLink: {
      pattern: 'https://github.com/XMOJ-Script-dev/docs/edit/master/:path',
      text: '在 GitHub 上编辑此页',
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
