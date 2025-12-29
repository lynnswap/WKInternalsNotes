# ``WKInternalsNotes/_WKTargetedElementInfo/inShadowTree``

シャドウツリー内かを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, getter=isInShadowTree) BOOL inShadowTree;
```

## Default Value
`API::TargetedElementInfo::isInShadowTree()` の値。

## Discussion
内部の `_info` から `isInShadowTree()` を取得して返す。

## References
- [`_WKTargetedElementInfo.h#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTargetedElementInfo.h#L48)
- [`_WKTargetedElementInfo.mm#L182`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTargetedElementInfo.mm#L182)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
