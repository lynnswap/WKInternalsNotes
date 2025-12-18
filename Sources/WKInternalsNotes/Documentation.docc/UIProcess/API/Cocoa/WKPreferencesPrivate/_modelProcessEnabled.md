# ``WKInternalsNotes/WKPreferences/_modelProcessEnabled``

Model Process を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setModelProcessEnabled:) BOOL _modelProcessEnabled WK_API_AVAILABLE(macos(15.4), ios(18.4), visionos(2.4));
```

## Default Value
iOS: `YES` / macOS: `YES` / visionOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_modelProcessEnabled = YES`: Model Process を有効化する。
- `_modelProcessEnabled = NO`: Model Process を無効化する。
- Implementation: [`HTMLModelElement.idl#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/model-element/HTMLModelElement.idl#L45)（`EnabledBySetting=ModelProcessEnabled`）

## Details
- WebPreferences key: `ModelProcessEnabled`

## References
- [`WKPreferencesPrivate.h#L201`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L201)
- [`WKPreferences.mm#L1698`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1698)
- [`HTMLModelElement.idl`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/model-element/HTMLModelElement.idl)
- [`UnifiedWebPreferences.yaml#L5414`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L5414) (key: `ModelProcessEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
