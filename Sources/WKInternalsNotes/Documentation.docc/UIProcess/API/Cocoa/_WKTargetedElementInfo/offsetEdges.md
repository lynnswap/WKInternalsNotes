# ``WKInternalsNotes/_WKTargetedElementInfo/offsetEdges``

オフセットされた辺をビットマスクで返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) _WKRectEdge offsetEdges;
```

## Default Value
`API::TargetedElementInfo::offsetEdges()` を `_WKRectEdge` に変換した値。

## Discussion
`offsetEdges()` の top/left/bottom/right を `_WKRectEdge` のフラグに変換して返す。

## References
- [`_WKTargetedElementInfo.h#L59`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTargetedElementInfo.h#L59)
- [`_WKTargetedElementInfo.mm#L123`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTargetedElementInfo.mm#L123)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
