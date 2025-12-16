# ``WKInternalsNotes/WKPreferencesPrivate/_modelElementEnabled``

HTML <model> element を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setModelElementEnabled:) BOOL _modelElementEnabled WK_API_AVAILABLE(macos(15.4), ios(18.4), visionos(2.4));
```

## Default Value
条件付き: ` (PLATFORM(VISION) || ENABLE(GPU_PROCESS_MODEL)) && ENABLE(MODEL_ELEMENT): YES / default: NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_modelElementEnabled = YES`: HTML <model> element を有効化する。
- `_modelElementEnabled = NO`: HTML <model> element を無効化する。
- Implementation: [`Source/WebCore/Modules/model-element/HTMLModelElement.idl#L28`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/model-element/HTMLModelElement.idl#L28)（`EnabledBySetting=ModelElementEnabled`）

## Details
- WebPreferences key: `ModelElementEnabled`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L200`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L200)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1708`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1708)
- [`Source/WebCore/Modules/model-element/HTMLModelElement.idl`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/model-element/HTMLModelElement.idl)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L5379`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L5379) (key: `ModelElementEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
