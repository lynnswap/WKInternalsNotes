# ``WKInternalsNotes/_WKTargetedElementInfo/boundsInClientCoordinates``

クライアント座標系での矩形を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) CGRect boundsInClientCoordinates;
```

## Default Value
`API::TargetedElementInfo::boundsInClientCoordinates()` の値。

## Discussion
内部の `_info` から `boundsInClientCoordinates()` を取得して返す。

## References
- [`_WKTargetedElementInfo.h#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTargetedElementInfo.h#L45)
- [`_WKTargetedElementInfo.mm#L75`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTargetedElementInfo.mm#L75)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
