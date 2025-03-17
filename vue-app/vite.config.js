import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

export default defineConfig({
  plugins: [vue()],

  server: {
    host: true, // 允许局域网访问
    port: 5173, // Vite 默认端口
    strictPort: true, // 确保使用这个端口
    cors: true, // 允许跨域

    proxy: {
      '/api': {
        target: 'http://192.168.0.227:8080',  // Flask 服务器
        changeOrigin: true,
        secure: false,
        rewrite: (path) => path.replace(/^\/api/, ''), // 去掉 /api 前缀
      },
    },
  },

  build: {
    outDir: "dist", // 确保 Vite 编译后的文件存入 dist 文件夹
    emptyOutDir: true, // 清空 dist 目录后再进行构建，避免旧文件影响
  }
});
