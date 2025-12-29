# ``WKInternalsNotes/_WKProcessPoolConfiguration/customWebContentServiceBundleIdentifier``

カスタム WebContent サービス識別子を返すが、現在は常に `nil`。

## Objective-C Declaration
```objective-c
@property (nonatomic, nullable, copy) NSString *customWebContentServiceBundleIdentifier WK_API_DEPRECATED("No longer supported", macos(10.14.4, 14.0), ios(12.2, 17.0));
```

## Default Value
常に `nil` を返す。

## Discussion
getter は `nil` を返し、setter は何もしないため、設定しても効果はない。

## References
- [`_WKProcessPoolConfiguration.mm#L353`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L353)
- [`_WKProcessPoolConfiguration.mm#L358`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L358)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
