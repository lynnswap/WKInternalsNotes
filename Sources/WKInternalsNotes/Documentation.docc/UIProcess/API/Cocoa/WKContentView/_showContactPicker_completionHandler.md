# ``WKInternalsNotes/WKContentView/_showContactPicker(_:completionHandler:)``

連絡先ピッカーを表示する。

## Objective-C Declaration
```objective-c
- (void)_showContactPicker:(const WebCore::ContactsRequestData&)requestData completionHandler:(WTF::CompletionHandler<void(std::optional<Vector<WebCore::ContactInfo>>&&)>&&)completionHandler;
```

## Discussion
ContactsUI が利用可能な場合は `WKContactPicker` を生成して delegate を設定し、`presentWithRequestData:completionHandler:` で表示する。未対応環境では `completionHandler` に `std::nullopt` を返す。

## References
- [`WKContentViewInteraction.h#L831`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L831)
- [`WKContentViewInteraction.mm#L9782`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L9782)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
