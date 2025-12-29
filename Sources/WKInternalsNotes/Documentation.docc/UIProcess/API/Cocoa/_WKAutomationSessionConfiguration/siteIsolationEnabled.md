# ``WKInternalsNotes/_WKAutomationSessionConfiguration/siteIsolationEnabled``

サイト分離を有効にするかを設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL siteIsolationEnabled;
```

## Default Value
`NO`。

## Discussion
`init` で `NO` に初期化され、`copyWithZone:` で現在の値が複製される。

## References
- [`_WKAutomationSessionConfiguration.h#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSessionConfiguration.h#L39)
- [`_WKAutomationSessionConfiguration.mm#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSessionConfiguration.mm#L41)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
