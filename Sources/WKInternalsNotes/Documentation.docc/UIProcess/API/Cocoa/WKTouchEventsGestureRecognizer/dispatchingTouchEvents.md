# ``WKInternalsNotes/WKTouchEventsGestureRecognizer/dispatchingTouchEvents``

タッチイベントの記録中であることを示すフラグ。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, getter=isDispatchingTouchEvents) BOOL dispatchingTouchEvents;
```

## Default Value
`reset` で `NO` に戻される。

## Discussion
`_recordTouches` で `YES` に設定される。`reset` で `NO` に戻る。

## References
- [`WKTouchEventsGestureRecognizer.h#L75`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTouchEventsGestureRecognizer.h#L75)
- [`WKTouchEventsGestureRecognizer.mm#L63`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTouchEventsGestureRecognizer.mm#L63)
- [`WKTouchEventsGestureRecognizer.mm#L108`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTouchEventsGestureRecognizer.mm#L108)
- [`WKTouchEventsGestureRecognizer.mm#L289`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTouchEventsGestureRecognizer.mm#L289)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
