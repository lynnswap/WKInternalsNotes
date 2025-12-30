# ``WKInternalsNotes/WKTouchEventsGestureRecognizer/defaultPrevented``

タッチイベントの既定動作を抑止したかを示すフラグ。

## Objective-C Declaration
```objective-c
@property (nonatomic, getter=isDefaultPrevented) BOOL defaultPrevented;
```

## Default Value
`reset` で `NO` に戻される。

## Discussion
`_processTouches` 内で `YES` の場合に recognizer の状態を `Began` / `Changed` に設定し、他の recognizer をキャンセルさせる。

## References
- [`WKTouchEventsGestureRecognizer.h#L72`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTouchEventsGestureRecognizer.h#L72)
- [`WKTouchEventsGestureRecognizer.mm#L62`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTouchEventsGestureRecognizer.mm#L62)
- [`WKTouchEventsGestureRecognizer.mm#L107`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTouchEventsGestureRecognizer.mm#L107)
- [`WKTouchEventsGestureRecognizer.mm#L485`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTouchEventsGestureRecognizer.mm#L485)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
