# ``WKInternalsNotes/_WKAutomationSessionConfiguration/allowsInsecureMediaCapture``

自動化セッションで安全でないメディアキャプチャを許可するかを設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL allowsInsecureMediaCapture;
```

## Default Value
`YES`。

## Discussion
`init` で `YES` に初期化され、`copyWithZone:` で現在の値が複製される。

## References
- [`_WKAutomationSessionConfiguration.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSessionConfiguration.h#L36)
- [`_WKAutomationSessionConfiguration.mm#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSessionConfiguration.mm#L38)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
