# ``WKInternalsNotes/_WKTargetedElementInfo/bounds``

root view 座標系の矩形を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) CGRect bounds;
```

## Default Value
`API::TargetedElementInfo::boundsInRootView()` の値。

## Discussion
内部の `_info` から `boundsInRootView()` を取得して返す。

## References
- [`_WKTargetedElementInfo.h#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTargetedElementInfo.h#L44)
- [`_WKTargetedElementInfo.mm#L70`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTargetedElementInfo.mm#L70)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
