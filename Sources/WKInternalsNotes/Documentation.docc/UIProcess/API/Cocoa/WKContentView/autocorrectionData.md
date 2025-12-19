# ``WKInternalsNotes/WKContentView/autocorrectionData``

オートコレクション用の内部データを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) const WebKit::WKAutoCorrectionData& autocorrectionData;
```

## Default Value
未調査（初期化経路の確認が必要）。

## Discussion
補正対象の矩形やフォントなど、オートコレクション処理で利用する `WKAutoCorrectionData` を参照する。

## References
- [`WKContentViewInteraction.h#L509`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L509)
- [`WKContentViewInteraction.mm#L5529`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L5529)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
