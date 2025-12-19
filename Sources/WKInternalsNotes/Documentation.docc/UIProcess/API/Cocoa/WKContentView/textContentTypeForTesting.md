# ``WKInternalsNotes/WKContentView/textContentTypeForTesting``

テスト用に現在の textContentType を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSString *textContentTypeForTesting;
```

## Default Value
表示中の入力 UI があればそこから取得し、無ければ textInputTraits 由来の値を返す。

## Discussion
PEPPER UI では表示中の入力ビュー（`WKTextInputListViewController` / Quickboard）から取得する。BrowserEngineKit 使用時に legacy traits を使わない場合は `extendedTraitsDelegate.textContentType` を返し、最後に `textInputTraits.textContentType` を返す。

## References
- [`WKContentViewInteraction.h#L1061`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L1061)
- [`WKContentViewInteraction.mm#L14519`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14519)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
