# ``WKInternalsNotes/WKDigitalCredentialsPickerDelegate/digitalCredentialsPickerDidPresent(_:)``

ピッカーの表示完了を通知する。

## Objective-C Declaration
```objective-c
- (void)digitalCredentialsPickerDidPresent:(WKDigitalCredentialsPicker *)picker;
```

## Discussion
`presentWithRequestData:completionHandler:` 内で `respondsToSelector:` を確認した上で呼び出す。

## References
- [`WKDigitalCredentialsPicker.h#L54`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/DigitalCredentials/WKDigitalCredentialsPicker.h#L54)
- [`WKDigitalCredentialsPicker.mm#L289`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/DigitalCredentials/WKDigitalCredentialsPicker.mm#L289)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
