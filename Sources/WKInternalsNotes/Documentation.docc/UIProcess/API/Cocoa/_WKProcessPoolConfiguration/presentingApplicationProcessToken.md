# ``WKInternalsNotes/_WKProcessPoolConfiguration/presentingApplicationProcessToken``

提示元プロセスの `audit_token_t` を設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic) audit_token_t presentingApplicationProcessToken WK_API_AVAILABLE(macos(10.13), ios(11.3));
```

## Default Value
既定値は未設定（空の token）。

## Discussion
setter は `ProcessPoolConfiguration` に token を保存し、getter は未設定時にゼロ初期化の `audit_token_t` を返す。

## References
- [`_WKProcessPoolConfiguration.mm#L224`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L224)
- [`_WKProcessPoolConfiguration.mm#L229`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L229)
- [`APIProcessPoolConfiguration.h#L212`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/APIProcessPoolConfiguration.h#L212)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
