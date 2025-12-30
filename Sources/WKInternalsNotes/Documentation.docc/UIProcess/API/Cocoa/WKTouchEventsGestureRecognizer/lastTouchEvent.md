# ``WKInternalsNotes/WKTouchEventsGestureRecognizer/lastTouchEvent``

直近に記録した `WKTouchEvent` を参照する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) const WebKit::WKTouchEvent& lastTouchEvent;
```

## Default Value
`reset` で初期値に戻される。

## Discussion
getter は `_lastTouchEvent` を返す。`_recordTouches` がイベント内容を更新する。

## References
- [`WKTouchEventsGestureRecognizer.h#L74`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTouchEventsGestureRecognizer.h#L74)
- [`WKTouchEventsGestureRecognizer.mm#L116`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTouchEventsGestureRecognizer.mm#L116)
- [`WKTouchEventsGestureRecognizer.mm#L276`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTouchEventsGestureRecognizer.mm#L276)
- [`WKTouchEventsGestureRecognizer.mm#L550`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTouchEventsGestureRecognizer.mm#L550)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
