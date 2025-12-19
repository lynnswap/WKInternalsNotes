# ``WKInternalsNotes/WKContentView/_doneDeferringTouchStart(_:)``

タッチ開始のデファリングを終了する。

## Objective-C Declaration
```objective-c
- (void)_doneDeferringTouchStart:(BOOL)preventNativeGestures;
```

## Discussion
`_touchStartDeferringGestures` を列挙して `endDeferral` を実行し、許可される場合は失敗扱いのジェスチャを記録する。

## References
- [`WKContentViewInteraction.h#L793`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L793)
- [`WKContentViewInteraction.mm#L2514`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L2514)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
