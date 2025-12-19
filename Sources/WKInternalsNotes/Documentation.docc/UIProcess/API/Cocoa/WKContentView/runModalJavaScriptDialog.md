# ``WKInternalsNotes/WKContentView/runModalJavaScriptDialog(_:)``

モーダルな JavaScript ダイアログ処理を実行する。

## Objective-C Declaration
```objective-c
- (void)runModalJavaScriptDialog:(CompletionHandler<void()>&&)callback;
```

## Discussion
キーボードでフォーカス移動中ならコールバックを保留し、それ以外は即座に実行する。

## References
- [`WKContentViewInteraction.h#L885`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L885)
- [`WKContentViewInteraction.mm#L6120`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L6120)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
