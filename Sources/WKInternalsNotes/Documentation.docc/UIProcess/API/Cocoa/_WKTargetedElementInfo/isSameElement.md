# ``WKInternalsNotes/_WKTargetedElementInfo/isSameElement(_:)``

同一要素かどうかを比較する。

## Objective-C Declaration
```objective-c
- (BOOL)isSameElement:(_WKTargetedElementInfo *)other;
```

## Discussion
`_info->isSameElement(*other->_info)` の結果を返す。

## References
- [`_WKTargetedElementInfo.h#L64`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTargetedElementInfo.h#L64)
- [`_WKTargetedElementInfo.mm#L147`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTargetedElementInfo.mm#L147)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
