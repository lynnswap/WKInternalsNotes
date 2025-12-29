# ``WKInternalsNotes/WKDigitalCredentialsPicker/dismissWithCompletionHandler(_:)``

デジタルクレデンシャル UI を閉じ、完了ハンドラに `true` を返す。

## Objective-C Declaration
```objective-c
- (void)dismissWithCompletionHandler:(CompletionHandler<void(bool)>&&)completionHandler;
```

## Discussion
`dismiss` を呼び出して UI を取り下げた後、`completionHandler(true)` を実行する。

## References
- [`WKDigitalCredentialsPicker.h#L65`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/DigitalCredentials/WKDigitalCredentialsPicker.h#L65)
- [`WKDigitalCredentialsPicker.mm#L292`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/DigitalCredentials/WKDigitalCredentialsPicker.mm#L292)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
