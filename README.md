## To use GUI for task

Enable the following in init()
```
if self.is_tasklist:
	self.taskgui=GUI_tasklist()
```

- 実行は`task_test.py`を参考
- passは従来のdrpの入力と同じ
- taskはエージェントへのタスクの割り当てを表し，サイズはエージェント数のリストとする．
	- 割り当てはタスクリスト`env.current_tasklist`の何番目のタスクかを表す（0~）
	- 割り当てを行わない場合は`-1`とする（例：`task = [-1,0,1,-1]`）