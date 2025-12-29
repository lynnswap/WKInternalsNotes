# ``WKInternalsNotes/WKDigitalCredentialsPicker/delegate``

表示/非表示の通知を受け取るデリゲート。

## Objective-C Declaration
```objective-c
@property (nonatomic, weak) id<WKDigitalCredentialsPickerDelegate> delegate;
```

## Default Value
`nil`。

## Discussion
内部では `WeakObjCPtr` として保持し、`presentWithRequestData:completionHandler:` と `dismiss` のタイミングで `digitalCredentialsPickerDidPresent:` / `digitalCredentialsPickerDidDismiss:` を呼び出す。

## References
- [`WKDigitalCredentialsPicker.h#L60`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/DigitalCredentials/WKDigitalCredentialsPicker.h#L60)
- [`WKDigitalCredentialsPicker.mm#L224`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/DigitalCredentials/WKDigitalCredentialsPicker.mm#L224)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
