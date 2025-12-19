# ``WKInternalsNotes/WKContentView/doAfterEditorStateUpdateAfterFocusingElement(_:)``

フォーカス後の editor state 更新を待って処理を実行する。

## Objective-C Declaration
```objective-c
- (void)doAfterEditorStateUpdateAfterFocusingElement:(dispatch_block_t)block;
```

## Discussion
更新待ちでなければ即時にブロックを実行し、待機中であれば後続実行キューに積む。

## References
- [`WKContentViewInteraction.h#L884`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L884)
- [`WKContentViewInteraction.mm#L8814`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L8814)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
