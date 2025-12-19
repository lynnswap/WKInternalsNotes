# ``WKInternalsNotes/WKContentView/_requestDOMPasteAccessForCategory(_:requiresInteraction:elementRect:originIdentifier:completionHandler:)``

宣言のみ確認（実装未調査）。

## Objective-C Declaration
```objective-c
- (void)_requestDOMPasteAccessForCategory:(WebCore::DOMPasteAccessCategory)pasteAccessCategory requiresInteraction:(WebCore::DOMPasteRequiresInteraction)requiresInteraction elementRect:(const WebCore::IntRect&)elementRect originIdentifier:(const String&)originIdentifier completionHandler:(CompletionHandler<void(WebCore::DOMPasteAccessResponse)>&&)completionHandler;
```

## Discussion
実装未調査。宣言と対応実装の確認が必要。

## References
- [`WKContentViewInteraction.h#L879`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L879)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
