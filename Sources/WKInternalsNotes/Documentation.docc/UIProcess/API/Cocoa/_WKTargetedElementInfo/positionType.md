# ``WKInternalsNotes/_WKTargetedElementInfo/positionType``

要素の positionType を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) _WKTargetedElementPosition positionType;
```

## Default Value
`API::TargetedElementInfo::positionType()` の値。

## Discussion
`WebCore::PositionType` を `_WKTargetedElementPosition`（Static/Relative/Absolute/Sticky/Fixed）に変換して返す。

## References
- [`_WKTargetedElementInfo.h#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTargetedElementInfo.h#L43)
- [`_WKTargetedElementInfo.mm#L54`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTargetedElementInfo.mm#L54)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
