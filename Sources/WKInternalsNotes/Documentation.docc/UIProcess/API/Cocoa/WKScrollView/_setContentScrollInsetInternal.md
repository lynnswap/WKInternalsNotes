# ``WKInternalsNotes/WKScrollView/_setContentScrollInsetInternal(_:)``

内部用の contentScrollInset を設定する。

## Objective-C Declaration
```objective-c
- (BOOL)_setContentScrollInsetInternal:(UIEdgeInsets)insets;
```

## Return Value
適用された場合は `YES`、無視された場合は `NO`。

## Discussion
外部で contentScrollInset が指定済みの場合や、同じ値が既に設定されている場合は無視される。watchOS では外部で contentInset が変更されている場合も無視される。適用時は内部値を更新し `contentScrollInset` を再計算する。

## References
- [`WKScrollView.h#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKScrollView.h#L44)
- [`WKScrollView.mm#L527`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKScrollView.mm#L527)
- [`WKScrollView.mm#L545`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKScrollView.mm#L545)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
