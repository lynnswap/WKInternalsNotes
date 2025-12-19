# ``WKInternalsNotes/WKScrollView/_setDecelerationRateInternal(_:)``

内部的に decelerationRate を設定する。

## Objective-C Declaration
```objective-c
- (void)_setDecelerationRateInternal:(UIScrollViewDecelerationRate)rate;
```

## Discussion
クライアントが `decelerationRate` を設定済みの場合は何もしない。未設定の場合のみ `super.decelerationRate` を更新する。

## References
- [`WKScrollView.h#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKScrollView.h#L45)
- [`WKScrollView.mm#L300`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKScrollView.mm#L300)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
