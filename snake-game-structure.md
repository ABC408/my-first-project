# 贪吃蛇游戏项目结构

## 目录结构

```
snake-game/
├── index.html           # 主页面
├── css/
│   └── style.css        # 样式文件
├── js/
│   ├── game.js          # 游戏主逻辑
│   ├── snake.js         # 蛇类定义
│   ├── food.js          # 食物类定义
│   └── utils.js         # 工具函数
└── README.md            # 项目说明文档
```

## 文件说明

### index.html
游戏主页面，包含Canvas元素和控制按钮

### css/style.css
游戏界面样式，包括布局和视觉效果

### js/game.js
游戏主控制器，负责游戏循环、状态管理和协调各组件

### js/snake.js
蛇类实现，包括移动、生长、绘制等逻辑

### js/food.js
食物类实现，包括生成、绘制等逻辑

### js/utils.js
通用工具函数，如随机数生成、碰撞检测等

### README.md
项目说明文档