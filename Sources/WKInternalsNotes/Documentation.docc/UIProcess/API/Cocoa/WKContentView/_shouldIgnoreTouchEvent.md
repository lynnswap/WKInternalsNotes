# ``WKInternalsNotes/WKContentView/_shouldIgnoreTouchEvent(_:)``

タッチイベントを無視すべきか判定する。

## Objective-C Declaration
```objective-c
- (BOOL)_shouldIgnoreTouchEvent:(UIEvent *)event;
```

## Discussion
`_touchEventsCanPreventNativeGestures` を `YES` に戻したうえで、画像解析インタラクション上のタッチや慣性スクロールの中断と判定される場合は `YES` を返す。

## References
- [`WKContentViewInteraction.h#L1003`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L1003)
- [`WKContentViewInteraction.mm#L9942`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L9942)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
