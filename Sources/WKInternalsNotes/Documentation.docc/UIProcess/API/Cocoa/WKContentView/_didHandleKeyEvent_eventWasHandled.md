# ``WKInternalsNotes/WKContentView/_didHandleKeyEvent(_:eventWasHandled:)``

キーイベント処理結果を反映する。

## Objective-C Declaration
```objective-c
- (void)_didHandleKeyEvent:(::WebEvent *)event eventWasHandled:(BOOL)eventWasHandled;
```

## Discussion
スクロールアニメータへの通知やアクティブキー処理状態を更新し、待機中の完了ハンドラに処理結果を返す。

## References
- [`WKContentViewInteraction.h#L840`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L840)
- [`WKContentViewInteraction.mm#L7719`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L7719)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
