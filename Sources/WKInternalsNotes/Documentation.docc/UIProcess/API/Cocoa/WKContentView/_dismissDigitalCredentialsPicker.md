# ``WKInternalsNotes/WKContentView/_dismissDigitalCredentialsPicker(_:)``

デジタルクレデンシャルピッカーを閉じる。

## Objective-C Declaration
```objective-c
- (void)_dismissDigitalCredentialsPicker:(CompletionHandler<void(bool)>&&)completionHandler;
```

## Discussion
ピッカーが表示されていなければログを残し、`completionHandler(false)` を返す。表示中なら `dismissWithCompletionHandler:` を呼ぶ。

## References
- [`WKContentViewInteraction.h#L835`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L835)
- [`WKContentViewInteraction.mm#L9771`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L9771)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
