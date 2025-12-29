# ``WKInternalsNotes/_WKTargetedElementInfo/hasLargeReplacedDescendant``

大きな置換要素の子孫を持つかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL hasLargeReplacedDescendant;
```

## Default Value
`API::TargetedElementInfo::hasLargeReplacedDescendant()` の値。

## Discussion
内部の `_info` から `hasLargeReplacedDescendant()` を取得して返す。

## References
- [`_WKTargetedElementInfo.h#L50`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTargetedElementInfo.h#L50)
- [`_WKTargetedElementInfo.mm#L162`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTargetedElementInfo.mm#L162)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
