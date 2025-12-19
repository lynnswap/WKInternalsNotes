# ``WKInternalsNotes/WKScrollView/_resetContentInsetAdjustmentBehavior()``

`contentInsetAdjustmentBehavior` の外部上書き状態を解除する。

## Objective-C Declaration
```objective-c
- (void)_resetContentInsetAdjustmentBehavior;
```

## Discussion
外部上書きフラグを `NO` に戻し、`UIScrollViewContentInsetAdjustmentAutomatic` を内部設定する。

## References
- [`WKScrollView.h#L54`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKScrollView.h#L54)
- [`WKScrollView.mm#L366`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKScrollView.mm#L366)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
