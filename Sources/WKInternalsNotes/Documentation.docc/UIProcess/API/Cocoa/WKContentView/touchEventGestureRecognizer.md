# ``WKInternalsNotes/WKContentView/touchEventGestureRecognizer``

タッチイベントの収集に使う `WKTouchEventsGestureRecognizer` を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) WKTouchEventsGestureRecognizer *touchEventGestureRecognizer;
```

## Default Value
`setUpInteraction` で生成した `WKTouchEventsGestureRecognizer` を返す。

## Discussion
`setUpInteraction` で `initWithContentView:` を用いて生成し、delegate を設定して `self` に追加する。getter は `_touchEventGestureRecognizer` を返す。

## References
- [`WKContentViewInteraction.h#L347`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L347)
- [`WKContentViewInteraction.mm#L1374`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L1374)
- [`WKContentViewInteraction.mm#L2463`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L2463)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
