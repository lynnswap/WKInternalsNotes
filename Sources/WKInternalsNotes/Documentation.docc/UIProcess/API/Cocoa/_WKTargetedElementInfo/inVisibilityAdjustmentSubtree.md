# ``WKInternalsNotes/_WKTargetedElementInfo/inVisibilityAdjustmentSubtree``

可視性調整サブツリー内かを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, getter=isInVisibilityAdjustmentSubtree) BOOL inVisibilityAdjustmentSubtree;
```

## Default Value
`API::TargetedElementInfo::isInVisibilityAdjustmentSubtree()` の値。

## Discussion
内部の `_info` から `isInVisibilityAdjustmentSubtree()` を取得して返す。

## References
- [`_WKTargetedElementInfo.h#L49`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTargetedElementInfo.h#L49)
- [`_WKTargetedElementInfo.mm#L157`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTargetedElementInfo.mm#L157)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
