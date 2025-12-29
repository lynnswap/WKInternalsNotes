# ``WKInternalsNotes/_WKInspectorExtension/extensionID``

拡張の識別子を返す。

## Objective-C Declaration
```objective-c
@property (readonly, nonatomic) NSString *extensionID;
```

## Default Value
`API::InspectorExtension::identifier()` の値。

## Discussion
内部の `_extension` から `identifier()` を取得して `NSString` 化して返す。

## References
- [`_WKInspectorExtension.h#L95`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorExtension.h#L95)
- [`_WKInspectorExtension.mm#L156`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorExtension.mm#L156)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
