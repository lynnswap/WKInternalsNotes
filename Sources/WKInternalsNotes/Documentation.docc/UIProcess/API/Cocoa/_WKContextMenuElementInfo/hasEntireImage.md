# ``WKInternalsNotes/_WKContextMenuElementInfo/hasEntireImage``

対象が画像全体を含むかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL hasEntireImage WK_API_AVAILABLE(macos(14.0));
```

## Default Value
`false`。

## Discussion
`ContextMenuContextData` の `hasEntireImage` を保持した値を返す。

## References
- [`_WKContextMenuElementInfo.mm#L66`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKContextMenuElementInfo.mm#L66)
- [`APIContextMenuElementInfoMac.h#L60`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/APIContextMenuElementInfoMac.h#L60)
- [`_WKContextMenuElementInfo.h#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKContextMenuElementInfo.h#L39)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
