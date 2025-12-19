# ``WKInternalsNotes/_WKLinkIconParameters/size``

リンクアイコンのサイズを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSNumber *size;
```

## Default Value
`linkIcon.size` が無い場合は `nil`。

## Discussion
`linkIcon.size` が存在する場合のみ `NSNumber` として保持する。

## References
- [`_WKLinkIconParameters.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKLinkIconParameters.h#L42)
- [`_WKLinkIconParameters.mm#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKLinkIconParameters.mm#L47)
- [`_WKLinkIconParameters.mm#L79`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKLinkIconParameters.mm#L79)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
