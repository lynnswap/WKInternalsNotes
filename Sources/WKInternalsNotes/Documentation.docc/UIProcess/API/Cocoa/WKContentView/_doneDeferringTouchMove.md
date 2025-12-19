# ``WKInternalsNotes/WKContentView/_doneDeferringTouchMove(_:)``

タッチ移動のデファリングを終了する。

## Objective-C Declaration
```objective-c
- (void)_doneDeferringTouchMove:(BOOL)preventNativeGestures;
```

## Discussion
`_touchMoveDeferringGestureRecognizer` に `endDeferral` を伝える。

## References
- [`WKContentViewInteraction.h#L794`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L794)
- [`WKContentViewInteraction.mm#L2523`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L2523)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
