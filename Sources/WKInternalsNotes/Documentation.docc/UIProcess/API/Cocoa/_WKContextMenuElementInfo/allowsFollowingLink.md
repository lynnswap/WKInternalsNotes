# ``WKInternalsNotes/_WKContextMenuElementInfo/allowsFollowingLink``

リンクの追従（開く）を許可するかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL allowsFollowingLink WK_API_AVAILABLE(macos(26.0));
```

## Default Value
`false`。

## Discussion
`ContextMenuContextData` の `allowsFollowingLink` を保持した値を返す。

## References
- [`_WKContextMenuElementInfo.mm#L71`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKContextMenuElementInfo.mm#L71)
- [`APIContextMenuElementInfoMac.h#L61`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/APIContextMenuElementInfoMac.h#L61)
- [`_WKContextMenuElementInfo.h#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKContextMenuElementInfo.h#L40)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
