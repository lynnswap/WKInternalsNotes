# ``WKInternalsNotes/WKContentView/_didUpdateEditorState()``

editor state 更新後の後処理を行う。

## Objective-C Declaration
```objective-c
- (void)_didUpdateEditorState;
```

## Discussion
初期書字方向の更新を確認し、フォーカス要素の表示調整待ちを解放する。保留中のブロックを実行して待機処理を完了する。

## References
- [`WKContentViewInteraction.h#L814`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L814)
- [`WKContentViewInteraction.mm#L8848`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L8848)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
