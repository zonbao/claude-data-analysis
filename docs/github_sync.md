# 将本地分支推送到你的 GitHub 仓库

如果你在本地已经有提交，但 GitHub 上看不到更新，通常是因为还没有配置远程或没有执行推送。按照下面的步骤即可把当前分支同步到你的 GitHub 仓库。

## 1. 检查是否已配置远程
```bash
git remote -v
```
- 如果没有输出，说明还未配置远程；继续下一步添加远程。
- 如果已显示远程，确认 URL 是否与你的 GitHub 仓库一致。

## 2. 添加远程（如未配置）
将 `<YOUR_GITHUB_URL>` 替换为你的仓库地址，例如 `https://github.com/zonbao/claude-data-analysis`：
```bash
git remote add origin <YOUR_GITHUB_URL>
```

## 3. 推送当前分支到远程
假设当前分支名为 `work`，执行：
```bash
git push -u origin work
```
- `-u` 会将本地分支与远程分支建立跟踪关系，之后可以直接使用 `git push`。
- 如果提示认证失败，需先在终端完成 GitHub 登录或使用 PAT（个人访问令牌）。

## 4. 验证推送是否成功
```bash
git status -sb
# 若显示 "## work" 且无未提交修改，说明本地工作区干净。
```
然后在 GitHub 仓库页面刷新查看提交记录即可。

## 5. 常见问题
- **远程已存在同名分支**：可先 `git fetch origin`，再决定是 `git pull --rebase` 合并远端更新，或用新分支名推送。
- **误加远程地址**：使用 `git remote set-url origin <YOUR_GITHUB_URL>` 更换；或 `git remote remove origin` 后重新添加。
- **网络/权限问题**：确认网络可访问 GitHub，并在推送前完成身份认证。
