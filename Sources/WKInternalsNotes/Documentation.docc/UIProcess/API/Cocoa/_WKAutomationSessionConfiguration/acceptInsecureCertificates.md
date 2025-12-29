# ``WKInternalsNotes/_WKAutomationSessionConfiguration/acceptInsecureCertificates``

自動化セッションで不正な証明書を受け入れるかどうかを設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL acceptInsecureCertificates;
```

## Default Value
`NO`。

## Discussion
`init` で `NO` に初期化され、`copyWithZone:` では現在の値が複製される。

## References
- [`_WKAutomationSessionConfiguration.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSessionConfiguration.h#L35)
- [`_WKAutomationSessionConfiguration.mm#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSessionConfiguration.mm#L37)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
