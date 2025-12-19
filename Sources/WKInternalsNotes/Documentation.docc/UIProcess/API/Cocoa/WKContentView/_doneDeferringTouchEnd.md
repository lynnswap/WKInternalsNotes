# ``WKInternalsNotes/WKContentView/_doneDeferringTouchEnd(_:)``

タッチ終了のデファリングを終了する。

## Objective-C Declaration
```objective-c
- (void)_doneDeferringTouchEnd:(BOOL)preventNativeGestures;
```

## Discussion
`_touchEndDeferringGestures` を列挙して `endDeferral` を実行する。

## References
- [`WKContentViewInteraction.h#L795`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L795)
- [`WKContentViewInteraction.mm#L2528`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L2528)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
