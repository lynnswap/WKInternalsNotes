# ``WKInternalsNotes/WKDigitalCredentialsPickerDelegate/digitalCredentialsPickerDidDismiss(_:)``

ピッカーの終了を通知する。

## Objective-C Declaration
```objective-c
- (void)digitalCredentialsPickerDidDismiss:(WKDigitalCredentialsPicker *)picker;
```

## Discussion
`dismiss` 内で `respondsToSelector:` を確認した上で呼び出す。

## References
- [`WKDigitalCredentialsPicker.h#L55`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/DigitalCredentials/WKDigitalCredentialsPicker.h#L55)
- [`WKDigitalCredentialsPicker.mm#L438`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/DigitalCredentials/WKDigitalCredentialsPicker.mm#L438)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
