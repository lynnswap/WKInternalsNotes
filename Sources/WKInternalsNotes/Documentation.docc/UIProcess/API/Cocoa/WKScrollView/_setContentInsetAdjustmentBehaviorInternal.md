# ``WKInternalsNotes/WKScrollView/_setContentInsetAdjustmentBehaviorInternal(_:)``

内部的に `contentInsetAdjustmentBehavior` を設定する。

## Objective-C Declaration
```objective-c
- (void)_setContentInsetAdjustmentBehaviorInternal:(UIScrollViewContentInsetAdjustmentBehavior)insetAdjustmentBehavior;
```

## Discussion
現在の値と同じなら何もしない。異なる場合のみ `super` の setter を呼び出す。

## References
- [`WKScrollView.h#L53`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKScrollView.h#L53)
- [`WKScrollView.mm#L358`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKScrollView.mm#L358)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
